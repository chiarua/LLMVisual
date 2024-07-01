import { Dict } from '../../util';
import { Scorer } from './base';
import { SpecQueryModel } from '../../model';
import { Schema } from '../../schema';
import { QueryConfig } from '../../config';
import { FeatureScore } from '../ranking';
/**
 * Penalize if facet channels are the only dimensions
 */
export declare class DimensionScorer extends Scorer {
    constructor();
    protected initScore(): Dict<number>;
    getScore(specM: SpecQueryModel, _: Schema, __: QueryConfig): FeatureScore[];
}
