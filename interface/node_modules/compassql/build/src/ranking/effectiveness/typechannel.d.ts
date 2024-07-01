import { QueryConfig } from '../../config';
import { SpecQueryModel } from '../../model';
import { Dict } from '../../util';
import { Schema } from '../../schema';
import { FeatureScore } from '../ranking';
import { ExtendedType } from './type';
import { Scorer } from './base';
import { Channel } from 'vega-lite/build/src/channel';
export declare const TERRIBLE = -10;
/**
 * Effectiveness score for relationship between
 * Field Type (with Bin and TimeUnit) and Channel Score (Cleveland / Mackinlay based)
 */
export declare class TypeChannelScorer extends Scorer {
    constructor();
    protected initScore(): Dict<number>;
    featurize(type: ExtendedType, channel: Channel): string;
    getScore(specM: SpecQueryModel, schema: Schema, opt: QueryConfig): FeatureScore[];
}
