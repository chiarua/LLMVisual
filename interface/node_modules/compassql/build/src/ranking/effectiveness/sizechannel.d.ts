import { Dict } from '../../util';
import { Scorer } from './base';
import { SpecQueryModel } from '../../model';
import { Schema } from '../../schema';
import { QueryConfig } from '../../config';
import { FeatureScore } from '../ranking';
/**
 * Effectivenss score that penalize size for bar and tick
 */
export declare class SizeChannelScorer extends Scorer {
    constructor();
    protected initScore(): Dict<number>;
    getScore(specM: SpecQueryModel, _: Schema, __: QueryConfig): FeatureScore[];
}
